import common.filereader as fr 

# OK - out come the objects for this one. 
class CommandList():
    def __init__(self, lines): 
        self.lines = lines 
        self.current_line = 0 

    def end(self):
        return self.current_line >= len(self.lines) 

    def next(self): 
        self.current_line += 1 

    def get_line(self):
        return self.lines[self.current_line]

class File():

    def __init__(self, name, size):
        self.name = name 
        self.size = size  

class Dir(): 

    def __init__(self, name, parent):
        self.dirs = list() 
        self.files = list() 
        self.name = name 
        self.parent = parent 
        self.total_size = 0 

    def get_dir(self, dirname): 
        for dirobj in self.dirs:
            if dirobj.name == dirname:
                return dirobj 
        return None 

    def read_dir(self, cmdlist):
        while not cmdlist.end(): 
            line = cmdlist.get_line() 
            if ( line.startswith("$") ):
                break 
            elif( line.startswith("dir") ):
                dirname = line[3:].strip() 
                newdir = Dir(dirname, self)
                self.dirs.append(newdir) 
            else:
                size, filename = line.split(' ') 
                size = int(size) 
                newfile = File(filename, size) 
                self.files.append(newfile)
                self.add_total(size) 
            cmdlist.next() 

    def add_total(self, size): 
        self.total_size += size 
        if ( self.parent != None ):
            self.parent.add_total(size) 

def build_directories( filelines ): 

    cmdlist = CommandList(filelines) 
    root_dir = None 
    current_dir = None 

    while not cmdlist.end():

        line = cmdlist.get_line() 

        if ( line == '$ cd /' ):
            root_dir = Dir('/',None) 
            current_dir = root_dir 
            cmdlist.next() 
        elif ( line.startswith("$ ls") ): 
            cmdlist.next() 
            current_dir.read_dir(cmdlist) 
        elif ( line.startswith("$ cd") ):
            cd_dir = line[4:].strip() 
            if ( cd_dir == '..' ):
                current_dir = current_dir.parent 
            else: 
                current_dir = current_dir.get_dir(cd_dir) 
            cmdlist.next() 
        else:
            # ignore
            print(f"Warning - unrecognised command {line}")
            cmdlist.next()


    return root_dir 

# just need the sizes 
def get_dir_size_list(dir_list, dir):
    dir_list.append(dir.total_size)
    for subdir in dir.dirs : 
        get_dir_size_list(dir_list, subdir)             

def first(filename):

    filelines = fr.readfile(filename)

    rootdir = build_directories(filelines) 

    dir_list = list() 
    get_dir_size_list(dir_list, rootdir) 

    total = 0 
    for size in dir_list:

        if ( size <= 100000 ):
            total += size  

    print(f"Answer = {total}")
    
def second(filename):

    filelines = fr.readfile(filename)

    rootdir = build_directories(filelines) 

    dir_list = list() 
    get_dir_size_list(dir_list, rootdir)
    dir_list.sort()

    free_space = 70000000 - rootdir.total_size 
    space_required = 30000000 - free_space 
    answer = 0 

    for size in dir_list: 
        if ( size >= space_required ):
            answer = size
            break 

    print(f"Answer = {answer}")

if __name__ == '__main__': 

    first("input/input07.txt") 
    second("input/input07.txt") 
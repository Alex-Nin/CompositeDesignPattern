import sys

class Entry:
    def list(self):
        pass
    
    def listall(self, level=0):
        pass
    
    def count(self):
        pass
    
    def countall(self):
        pass
    
    def is_directory(self):
        return False

class File(Entry):
    def __init__(self, name):
        self.name = name

    def list(self):
        return self.name
    
    def count(self):
        return 1

class Directory(Entry):
    def __init__(self, name):
        self.name = name
        self.entries = {}
        self.parent = None

    def add_entry(self, entry):
        self.entries[entry.name] = entry
        if isinstance(entry, Directory):
            entry.parent = self

    def list(self):
        return ' '.join(self.entries.keys())
    
    def listall(self, level=0):
        output = '   ' * level + self.name + ':\n'
        for entry in self.entries.values():
            if entry.is_directory():
                output += entry.listall(level + 1)
            else:
                output += '   ' * (level + 1) + entry.list() + '\n'
        return output

    def count(self):
        return sum(1 for entry in self.entries.values() if not entry.is_directory())
    
    def countall(self):
        total = 0
        for entry in self.entries.values():
            if entry.is_directory():
                total += entry.countall()
            else:
                total += entry.count()
        return total

    def is_directory(self):
        return True

class FileSystem:
    def __init__(self, root):
        self.current_dir = root
        self.root = root

    def change_directory(self, dir_name):
        if dir_name == '..':
            if self.current_dir.parent:
                self.current_dir = self.current_dir.parent
        elif dir_name in self.current_dir.entries and self.current_dir.entries[dir_name].is_directory():
            self.current_dir = self.current_dir.entries[dir_name]
        else:
            print("no such directory")

    def execute_command(self, command):
        if command == 'list':
            print(self.current_dir.list())
        elif command == 'listall':
            print(self.current_dir.listall().strip())
        elif command.startswith('chdir'):
            _, dir_name = command.split(maxsplit=1)
            self.change_directory(dir_name)
        elif command == 'up':
            self.change_directory('..')
        elif command == 'count':
            print(self.current_dir.count())
        elif command == 'countall':
            print(self.current_dir.countall())
        elif command == 'q':
            sys.exit()
        else:
            print("invalid command")

def parse_directory(data):
    lines = data.strip().splitlines()
    root = Directory(lines[0].strip(':'))
    stack = [(root, 0)]
    
    for line in lines[1:]:
        depth = len(line) - len(line.lstrip())
        name = line.strip()
        
        if name.endswith(':'):
            dir_name = name.strip(':')
            dir_entry = Directory(dir_name)
            while stack and stack[-1][1] >= depth:
                stack.pop()
            stack[-1][0].add_entry(dir_entry)
            stack.append((dir_entry, depth))
        else:
            file_entry = File(name)
            stack[-1][0].add_entry(file_entry)
    
    return root

def main():
    with open('MyProg6TESTdirectory.dat') as f:
        data = f.read()

    root = parse_directory(data)
    fs = FileSystem(root)

    while True:
        command = input(f"{fs.current_dir.name}> ").strip()
        fs.execute_command(command)

if __name__ == '__main__':
    main()

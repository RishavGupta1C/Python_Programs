def main():
    N = int(input())
    list1 = []
    for _ in range(N):
        cmd = input().split()
        if len(cmd) == 1:
            command = cmd[0]
            if command == 'print':
                print(list1)
            elif command == 'sort':
                list1.sort()
            elif command == 'pop':
                list1.pop()
            elif command == 'reverse':
                list1.reverse()
                # list1=list(reversed(list1))
        elif len(cmd) == 2:
            command = cmd[0]
            element = int(cmd[1])
            if command == 'remove':
                list1.remove(element)
            elif command == 'append':
                list1.append(element)
        elif len(cmd) == 3:
            command = cmd[0]
            index = int(cmd[1])
            element = int(cmd[2])
            if command == 'insert':
                list1.insert(index, element)
        else:
            print("Invalid Command Format")
        # elif command == 'print':
        #     print(list1)
        # elif command == 'remove':
        #     list1.remove(element)
        # elif command == 'append':
        #     list1.append(element)
        # elif command == 'sort':
        #     list1.sort()
        # elif command == 'pop':
        #     list1.pop()
        # elif command == 'reverse':
        #     list1.reverse()
        # else:
        #     print("Invalid Command")

main()
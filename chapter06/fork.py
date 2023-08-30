from collections import deque

fork = {"you": ["alice", "bob", "claire"], "bob": ["anuj", "peggy"], "alice": ["peggy"],
        "claire": ["thom", "jonny", "mary"],
        "anuj": [], "peggy": [], "thom": [], "jonny": []}


def people_is_a_saller(name):
    return name[-1] == 'y'


def search(name):
    search_queue = deque()
    search_queue += fork[name]
    verify = []
    while search_queue:
        print(fork)
        people = search_queue.popleft()
        if not people in verify:
            if people_is_a_saller(people):
                print(people + " é um vendedor de manga!")
                return True
            else:
                search_queue += fork[people]
                verify.append(people)
        return False


search("you")

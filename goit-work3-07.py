def first(size, *topics):
    size = len(topics) + size
    print(size)
    return size


def second(size, **zopics):
    size = len(zopics) + size
    print(size)
    return size

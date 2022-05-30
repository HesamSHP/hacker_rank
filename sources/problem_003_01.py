if __name__ == '__main__':
    message = f"The Government of Iran is an Islamic theocracy which includes elements of a presidential democracy, with the ultimate authority vested in an autocratic \"Supreme Leader\" a position held by Ali Khamenei since Khomeini's death in 1989. The Iranian government is widely considered to be authoritarian, and has attracted widespread criticism for its significant constraints and abuses against human rights and civil liberties including several violent suppressions of mass protests, unfair elections, and limited rights for women and children. It is also a focal point for Shia Islam within the Middle East, countering the long-existing Arab Sunni hegemony within the region, and is often considered Israel's largest adversary. The state is considered one of the biggest players within Middle Eastern affairs, with its government directly or indirectly involved in a majority of modern Middle Eastern conflicts"
    my_dict = {}
    for item in message.split():
        my_dict.setdefault(item, 0)
        my_dict[item] += 1

    print(my_dict)


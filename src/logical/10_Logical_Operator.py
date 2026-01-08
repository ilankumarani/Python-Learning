
def main():
    has_id = True
    is_banned = False
    is_admin = False

    if (has_id and not is_banned) or is_admin:
        print("Entry allowed")
    else:
        print("Entry denied")


if __name__ == "__main__":
    main()

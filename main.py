import pi_connector


def main():
    pi_connector.setup_callbacks('192.168.1.13', [26])

    # Loop and wait for events
    while True:
        pass

if __name__ == "__main__":
    main()
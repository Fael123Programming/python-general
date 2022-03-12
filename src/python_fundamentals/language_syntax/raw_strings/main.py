if __name__ == "__main__":
    print(r"C:\some\name")
    print("C:\some\name")
    print("""\
Usage: thingy [OPTIONS]
    -h                  Display this usage message
    -H                  Hostname to connect to
    """
          )
    print("un" + "bled" * 5)  # You may concatenate only strings.
    print("un" "bled" * 5)
    text = ('Put several long strings together'
            ' inside a parentheses'
            ' to have them joined')
    print(text)

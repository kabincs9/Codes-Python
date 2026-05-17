import sys

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

    print(f"hello, {sys.argv[1]}")
    sys.exit(0)

# if we run ...py we wil get like missing ..
#if we write( echo $?) then 1 wil come then again running will show hello, our name

# in first commandlinegreet.py

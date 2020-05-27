import sys
import lorem

cantidad_parrafos = int(sys.argv[1])

while cantidad_parrafos > 0:
    print(lorem.paragraph())
    print()
    cantidad_parrafos -= 1
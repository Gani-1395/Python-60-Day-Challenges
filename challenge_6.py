m = input("enter your favourite number: ")
if m.isdigit():
    n = int(input("Enter number of songs: "))
    data = [0] * n
    dup = 0
    total = 0
    for i in range(n):
        data[i] = int(input())
        if data[i] <= 0:
            print("Invalid Playlist")
            break
        total += data[i]
    else:
        for i in range(n):
            for j in range(i + 1, n):
                if data[i] == data[j]:
                    dup += 1
        if total < 300:
            print("Category: Too Short Playlist")
            print("Recommendation: Add more songs")
        elif total > 3600:
            print("Category: Too Long Playlist")
            print("Recommendation: Take a Break")
        elif dup > 0:
            print("Category: Repetitive Playlist")
            print("Recommendation: Add variety")
        elif total >= 300 and total <= 3600:
            print("Total Duration:", total, "seconds")
            print("Songs:", n)
            print("Category: Balanced Playlist")
            print("Recommendation: Good listening session")
        else:
            print("Category: Irregular Playlist")
            print("Recommendation: Work on song selection")
else:
    print("invalid number")
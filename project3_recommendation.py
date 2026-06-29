print("=== Movie Recommendation System ===")

genre = input("Enter your favorite genre (action/comedy/horror): ").lower()

if genre == "action":
    print("Recommended Movies:")
    print("- Avengers")
    print("- John Wick")
    print("- Mission Impossible")

elif genre == "comedy":
    print("Recommended Movies:")
    print("- Mr. Bean")
    print("- Home Alone")
    print("- The Mask")

elif genre == "horror":
    print("Recommended Movies:")
    print("- The Conjuring")
    print("- Annabelle")
    print("- Insidious")

else:
    print("Sorry! No recommendations available for that genre.")

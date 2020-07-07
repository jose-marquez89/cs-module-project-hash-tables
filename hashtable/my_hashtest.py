from hashtable import HashTable

table = HashTable(10)

if __name__ == "__main__":
    table.put("Ionian", "C")
    table.put("Dorian", "D")
    table.put("Phrygian", "E")
    table.put("Lydian", "F")
    table.put("Mixolydian", "G")
    table.put("Aeolian", "A")
    table.put("Locrian", "B")

    table.put("Zandalorian", "Z")
    table.put("Xorolydian", "X")
    table.put("Hyrulian", "H")
    table.put("Partypartian", "P")

    print(table.get("Zandalorian"))
    print(table.get("Dorian"))
    print(table.get("Locrian"))

    table.delete("Zandalorian")
    table.delete("Xorolydian")
    table.delete("Hyrulian")
    table.delete("Partypartian")

    print(table.get("Partypartian"))
    print(table.get("Hyrulian"))
    print(table.get("Xorolydian"))
    print(table.get("Zandalorian"))

    table.delete("Zandalorian")
    table.delete("Xorolydian")
    table.delete("Hyrulian")
    table.delete("Partypartian")

    print(table.get("hahaha"))
    print(table.get("onetwothree"))

    table.delete("bobobo")

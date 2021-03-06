from hashtable import HashTable

table = HashTable(8)

if __name__ == "__main__":
    table.put("Ionian", "C")
    table.put("Dorian", "D")
    table.put("Phrygian", "E")
    table.put("Lydian", "F")
    table.put("Mixolydian", "G")
    table.put("Aeolian", "A")
    table.put("Locrian", "B")

    print("ENTRIES:")
    print(table.entries)

    table.put("Zandalorian", "Z")
    table.put("Xorolydian", "X")
    table.put("Hyrulian", "H")
    table.put("Partypartian", "P")

    print("ENTRIES:")
    print(table.entries)

    print(table.get("Zandalorian"))
    print(table.get("Dorian"))
    print(table.get("Locrian"))

    table.delete("Zandalorian")
    table.delete("Xorolydian")
    table.delete("Hyrulian")
    table.delete("Partypartian")

    print("ENTRIES:")
    print(table.entries)

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

    table.put("Ionian", "This is not a note")
    print(table.get("Ionian"))

    print(table.get_load_factor())
    print(table.get_num_slots())
    print(table.entries)

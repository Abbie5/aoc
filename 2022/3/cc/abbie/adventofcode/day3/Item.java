package cc.abbie.adventofcode.day3;

class Item {
    private final char name;
    public Item(char name) {
        this.name = name;
    }
    public int priority() {
        int result;
        if (name <= (int) 'Z') {
            result = name - 'A' + 1 + 26;
        } else {
            result = name - 'a' + 1;
        }
        return result;
    }

    public char getName() {
        return name;
    }
}

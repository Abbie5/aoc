package cc.abbie.adventofcode.day3;

import java.util.ArrayList;
import java.util.List;

class Compartment {
    private final List<Item> items;
    public Compartment(String s) {
        items = new ArrayList<>();
        for (int i=0; i < s.length(); i++) {
            items.add(new Item(s.charAt(i)));
        }
    }

    public List<Item> getItems() {
        return items;
    }

    public List<Integer> getPriorities() {
        List<Integer> result = new ArrayList<>();
        for (Item item : getItems()) {
            result.add(item.priority());
        }
        return result;
    }

    @Override
    public String toString() {
        StringBuilder result = new StringBuilder();
        for (Item item : items) {
            result.append(item.getName());
        }
        return result.toString();
    }
}

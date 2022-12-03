package cc.abbie.adventofcode.day3;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Rucksack {
    private final Compartment leftCompartment;
    private final Compartment rightCompartment;

    public Rucksack(String s) {
        int length = s.length();
        leftCompartment = new Compartment(s.substring(0, length / 2));
        rightCompartment = new Compartment(s.substring(length / 2));
    }

    public Set<Integer> getDuplicatePriorities() {
        List<Integer> leftPriorities = leftCompartment.getPriorities();
        List<Integer> rightPriorities = rightCompartment.getPriorities();
        Set<Integer> priorities = new HashSet<>(leftPriorities);

        priorities.retainAll(rightPriorities);
        return priorities;
    }

    public int getSumOfDuplicatePriorities() {
        int total = 0;
        for (int priority : getDuplicatePriorities()) {
            total += priority;
        }
        return total;
    }
}
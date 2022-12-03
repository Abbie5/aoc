package cc.abbie.adventofcode.day3;

import java.util.*;

class Group {
    private final Compartment elf1;
    private final Compartment elf2;
    private final Compartment elf3;

    public Group(String s1, String s2, String s3) {
        elf1 = new Compartment(s1);
        elf2 = new Compartment(s2);
        elf3 = new Compartment(s3);
    }

    public Set<Integer> getDuplicatePriorities() {
        List<Integer> elf1Priorities = elf1.getPriorities();
        List<Integer> elf2Priorities = elf2.getPriorities();
        List<Integer> elf3Priorities = elf3.getPriorities();
        Set<Integer> priorities = new HashSet<>(elf1Priorities);
        priorities.retainAll(elf2Priorities);
        priorities.retainAll(elf3Priorities);

        return priorities;
    }
}
package cc.abbie.adventofcode.day3;

import java.util.Scanner;

public class Part2 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int total = 0;
        int i = 0;
        String[] elves = new String[3];
        while (in.hasNextLine()) {
            elves[i] = in.nextLine();
            if (i == 2) {
                Group group = new Group(
                        elves[0],
                        elves[1],
                        elves[2]
                );
                i = 0;
                total += group.getDuplicatePriorities().iterator().next();
            } else {
                i++;
            }
        }
        System.out.println(total);
    }
}

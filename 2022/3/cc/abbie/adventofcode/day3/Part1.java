package cc.abbie.adventofcode.day3;

import java.util.Scanner;

public class Part1 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int total = 0;
        while (in.hasNextLine()) {
            Rucksack rucksack = new Rucksack(in.nextLine());
            total += rucksack.getSumOfDuplicatePriorities();
        }
        System.out.println(total);
    }
}

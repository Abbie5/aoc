package cc.abbie.aoc.year2022.day5;

class Step {
    int count;
    int from;
    int to;

    Step(String s) {
        String[] words = s.split(" ");
        count = Integer.parseInt(words[1]);
        from = Integer.parseInt(words[3]);
        to = Integer.parseInt(words[5]);
    }
}

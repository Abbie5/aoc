package cc.abbie.aoc.year2022.day5;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

public class Main2 {
    public static void main(String[] args) throws IOException {
        String input = new String(Files.readAllBytes(Paths.get("C:\\Users\\Abbie\\Documents\\aoc\\2022\\5\\input.txt")));
        String[] parts = input.split("\\n\\n");
        String[] initialStateString = parts[0].split("\\n");
        String[] procedureString = parts[1].split("\\n");
        List<Step> procedure = new ArrayList<>();
        for (String line : procedureString) {
            procedure.add(new Step(line));
        }

        HashMap<Integer, Stack<Character>> state = new HashMap<>();

        List<String> newInitialState = new ArrayList<>();
        for (String line : initialStateString) {
            StringBuilder newLineBuilder = new StringBuilder();
            for (int i = 0; i < line.length(); i++) {
                if (i % 4 == 1) {
                    newLineBuilder.append(line.charAt(i));
                }
            }
            String newLine = newLineBuilder.toString();
//            System.out.println(newLine);
            newInitialState.add(newLine);
        }

        Collections.reverse(newInitialState);
        newInitialState.remove(0);
        for (String s : newInitialState) {
            for (int j = 0; j < s.length(); j++) {
                int stackNum = j + 1;
                if (!state.containsKey(stackNum)) state.put(stackNum, new Stack<>());
                char c = s.charAt(j);
                if (c != ' ') state.get(stackNum).add(c);
            }
        }

//        for (int key : state.keySet()) {
//            System.out.printf("%d %s\n", key, state.get(key).toString());
//        }

        for (Step step : procedure) {
            Stack<Character> q = new Stack<>();
            for (int i = 0; i < step.count; i++) {
                q.push(state.get(step.from).pop());
            }
            Collections.reverse(q);
            for (char asdf : q) {
                state.get(step.to).push(asdf);
            }
        }

        StringBuilder part1Builder = new StringBuilder();
        for (Iterator<Integer> it = state.keySet().stream().sorted().iterator(); it.hasNext(); ) {
            int key = it.next();
            part1Builder.append(state.get(key).peek());
        }
        System.out.println(part1Builder);

    }
}

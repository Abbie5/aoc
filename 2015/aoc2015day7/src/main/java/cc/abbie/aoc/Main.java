package cc.abbie.aoc;

import cc.abbie.aoc.operation.Operation;
import cc.abbie.aoc.operation.Operations;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;

public class Main {
    static HashMap<String, Statement> expressions = new HashMap<>();

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("example.txt"));

        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            String[] parts = line.split(" -> ");
            String statementString = parts[0];
            String wire = parts[1];
            expressions.put(wire, new Statement(statementString));
        }

        int a = solve(expressions.get("a"));

        System.out.println(a);

    }

    public static int solve(Statement statement) {
        Operation operation = statement.getOperation();
        Operand[] operands = statement.getOperands();
        if (operands.length == 1 && operation == Operations.IDENT) {
            return (int) operation.apply(operands).getValue();
        } else if (operands.length == 1) {
            return (int) operation.apply(new Operand[]{new Operand<>(solve(expressions.get(operands[0].getValue())))}).getValue();
        } else {
            return (int) operation.apply(new Operand[]{new Operand<>(solve(expressions.get(operands[0].getValue()))), new Operand<>(solve(expressions.get(operands[1].getValue())))}).getValue();
        }
    }
}
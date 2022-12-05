package cc.abbie.aoc.operation;

import cc.abbie.aoc.Operand;

public class And implements Operation {
    int numOperands = 2;

    private And() {}
    private static And INSTANCE;

    public static And getInstance() {
        return INSTANCE;
    }

    @Override
    public Operand<Integer> apply(Operand<Integer>[] operands) {
        return new Operand<>(operands[0].getValue() & operands[1].getValue());
    }
}

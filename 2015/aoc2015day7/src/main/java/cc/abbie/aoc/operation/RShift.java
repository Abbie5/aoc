package cc.abbie.aoc.operation;

import cc.abbie.aoc.Operand;

public class RShift implements Operation {
    int numOperands = 2;

    private RShift() {}
    private static RShift INSTANCE;

    public static RShift getInstance() {
        return INSTANCE;
    }


    @Override
    public Operand<Integer> apply(Operand<Integer>[] operands) {
        return new Operand<>(operands[0].getValue() >> operands[1].getValue());
    }

}

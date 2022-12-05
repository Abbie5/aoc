package cc.abbie.aoc.operation;

import cc.abbie.aoc.Operand;

public class LShift implements Operation {
    int numOperands = 2;

    private LShift() {}
    private static LShift INSTANCE;

    public static LShift getInstance() {
        return INSTANCE;
    }


    @Override
    public Operand<Integer> apply(Operand<Integer>[] operands) {
        return new Operand<>(operands[0].getValue() << operands[1].getValue());
    }

}

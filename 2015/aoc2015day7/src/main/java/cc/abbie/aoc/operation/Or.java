package cc.abbie.aoc.operation;

import cc.abbie.aoc.Operand;

public class Or implements Operation {
    int numOperands = 2;

    private Or() {}
    private static Or INSTANCE;

    public static Or getInstance() {
        return INSTANCE;
    }


    @Override
    public Operand<Integer> apply(Operand<Integer>[] operands) {
        return new Operand<>(operands[0].getValue() | operands[1].getValue());
    }

}

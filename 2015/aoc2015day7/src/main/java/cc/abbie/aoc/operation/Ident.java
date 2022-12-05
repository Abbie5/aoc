package cc.abbie.aoc.operation;

import cc.abbie.aoc.Operand;

public class Ident implements Operation {
    private Ident() {}
    private static Ident INSTANCE;

    public static Ident getInstance() {
        return INSTANCE;
    }

    @Override
    public Operand<Integer> apply(Operand<Integer>[] operands) {
        return operands[0];
    }
}

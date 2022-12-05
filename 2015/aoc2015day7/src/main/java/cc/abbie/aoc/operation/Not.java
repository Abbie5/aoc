package cc.abbie.aoc.operation;

import cc.abbie.aoc.Operand;

public class Not implements Operation {
    int numOperands = 1;

    private Not() {}
    private static Not INSTANCE;

    public static Not getInstance() {
        return INSTANCE;
    }


    @Override
    public Operand<Integer> apply(Operand<Integer>[] operands) {
        return new Operand<>(~operands[1].getValue());
    }

}

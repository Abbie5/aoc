package cc.abbie.aoc.operation;

import cc.abbie.aoc.Operand;

public interface Operation {
    Operand<Integer> apply(Operand<Integer>[] operands);
}

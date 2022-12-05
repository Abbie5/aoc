package cc.abbie.aoc;

public class Operand<T> {
    private T value;

    public Operand(T t) {
        value = t;
    }

    public T getValue() {
        return value;
    }
}

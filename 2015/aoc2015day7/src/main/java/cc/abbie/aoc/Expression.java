package cc.abbie.aoc;

public class Expression {
    Statement leftSide;
    String rightSide;

    public Expression(Statement l, String r) {
        leftSide = l;
        rightSide = r;
    }

    public Statement getLeftSide() {
        return leftSide;
    }

    public String getRightSide() {
        return rightSide;
    }
}

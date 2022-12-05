package cc.abbie.aoc.operation;

public record Operations() {
    public static Ident IDENT = Ident.getInstance();
    public static Not NOT = Not.getInstance();
    public static And AND = And.getInstance();
    public static Or OR = Or.getInstance();
    public static RShift RSHIFT = RShift.getInstance();
    public static LShift LSHIFT = LShift.getInstance();
}

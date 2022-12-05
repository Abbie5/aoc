package cc.abbie.aoc;

import cc.abbie.aoc.operation.Operation;
import cc.abbie.aoc.operation.Operations;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Statement {
    //private static final Pattern re = Pattern.compile("^(?<operand1>\\w+|) ?(?<operation>NOT|AND|OR|RSHIFT|LSHIFT|) ?(?<operand2>\\d+|\\w+)$");
    private static final Pattern identRe = Pattern.compile("^\\d+$");
    private static final Pattern notRe = Pattern.compile("^NOT (?<operand>\\w+)$");
    private static final Pattern otherRe = Pattern.compile("^(?<operand1>\\w+) (?<operation>AND|OR|RSHIFT|LSHIFT) (?<operand2>\\w+)$");
    private Operand[] operands;
    private Operation operation;

    public Statement(String s) {
        /*
        statement string matches one of
        <number>
        NOT <letters>
        <letters> <AND/OR/RSHIFT/LSHIFT> <letters>
         */

//        Matcher matcher = re.matcher(s);
//
//        String operand1 = matcher.group("operand1");
//        String operationString = matcher.group("operation");
//        String operand2 = matcher.group("operand2");

        if (identRe.matcher(s).matches()) {
            operation = Operations.IDENT;
            Operand<Integer> operand = new Operand<>(Integer.parseInt(s));
            operands = new Operand[]{operand};
        } else if (notRe.matcher(s).matches()) {
            Matcher matcher = notRe.matcher(s);
            matcher.find();
            operation = Operations.NOT;
            Operand<String> operand = new Operand<>(matcher.group("operand"));
            operands = new Operand[]{operand};
        } else {
            Matcher matcher = otherRe.matcher(s);
            matcher.find();
            System.out.println(s);
            String operationString = matcher.group("operation");
            String operand1 = matcher.group("operand1");
            String operand2 = matcher.group("operand2");

            if (operationString.compareTo("AND") == 0) {
                operation = Operations.AND;
            } else if (operationString.compareTo("OR") == 0) {
                operation = Operations.OR;
            } else if (operationString.compareTo("RSHIFT") == 0) {
                operation = Operations.RSHIFT;
            } else if (operationString.compareTo("LSHIFT") == 0) {
                operation = Operations.LSHIFT;
            }

            operands = new Operand[]{new Operand<>(operand1), new Operand<>(operand2)};
        }
    }

    public Operand[] getOperands() {
        return operands;
    }

    public Operation getOperation() {
        return operation;
    }
}

public abstract class Approver {
    public Approver nextApprover;

    public Approver setNextApprover(Approver nextApprover) {
        this.nextApprover = nextApprover;
        return nextApprover;
    }

    public abstract void processRequest(PurchaseRequest request);
}
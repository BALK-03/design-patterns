public class Client {
    public static void main(String[] args) {
        // Create the approvers
        Approver manager = new Manager();
        Approver director = new Director();
        Approver ceo = new CEO();

        // Build the chain of responsibility
        manager.setNextApprover(director);
        director.setNextApprover(ceo);

        // Process various requests
        manager.processRequest(new PurchaseRequest(101, 4500.0));   // Handled by Manager
        manager.processRequest(new PurchaseRequest(102, 15000.0));  // Handled by Director
        manager.processRequest(new PurchaseRequest(103, 35000.0));  // Handled by CEO
    }
}
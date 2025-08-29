public class TextDocument implements Document {
    @Override
    public void open() {
        System.out.println("Opening a plain text document.");
    }

    @Override
    public void save() {
        System.out.println("Closing a plain text document.");
    }
}
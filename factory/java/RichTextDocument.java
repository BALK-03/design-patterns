public class RichTextDocument implements Document {
    @Override
    public void open() {
        System.out.println("Opening a rich text document.");
    }
    @Override
    public void save() {
        System.out.println("Saving a rich text document.");
    }
}
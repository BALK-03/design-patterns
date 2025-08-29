public class RichTextApplication extends Application {
    @Override
    public Document createDocument() {
        return new RichTextDocument();
    }
}
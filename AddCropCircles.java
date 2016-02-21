//CARISSA WARD

import javax.imageio.ImageIO;
import java.io.File;
import javafx.scene.control.Button;
import javafx.scene.input.MouseEvent;
import javafx.application.Application;
import javafx.embed.swing.SwingFXUtils;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Point2D;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.image.PixelReader;
import javafx.scene.image.WritableImage;
import javafx.scene.layout.AnchorPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.stage.Stage;
import java.util.Random;
import java.awt.Point;
import java.util.ArrayList;
import java.util.List;

public class AddCropCircles extends Application
{
	AnchorPane root;
	ImageView cropsImageView;
	static String filename;
	Image cropsImage;
	
	int height = 0;
	int width = 0;
	

	
	public void start(Stage cropStage) throws Exception
	{
		root = new AnchorPane();
		loadImage();
		Scene scene = new Scene(root, width, height);
		
		cropStage.setScene(scene);
		cropStage.setTitle("With Crop Circles");
		cropStage.show();
		
	    scene.setOnMouseReleased(mouseHandler);
		
	    Button btn = new Button("Save");
	    
	    btn.setOnAction(new EventHandler<ActionEvent>(){
	    	@Override public void handle(ActionEvent e){
	    		createFile();	
	    	}
	    });
	    
	    root.getChildren().add(btn);
	    
			
	}
	
	private void loadImage()
	{
		cropsImage = new Image(filename);
		height = (int) cropsImage.getHeight();
		width = (int) cropsImage.getWidth();
		
		if (width> 2900 || height > 900)
		{
			cropsImage = new Image(filename,2900,950,true,true);
			height = (int) cropsImage.getHeight();
			width = (int) cropsImage.getWidth();
		}
		
		cropsImageView = new ImageView(cropsImage);
		cropsImageView.setX(0);
		cropsImageView.setY(0);
		root.getChildren().add(cropsImageView);
	}
	
	private void createRing(int x, int y, int r)
	{
		Circle circle = new Circle();
		circle.setCenterX(x);
		circle.setCenterY(y);
		circle.setRadius(r);
		
		List<Color> colorCollection = new ArrayList<Color>();
		List<Point> pointCollection = findCoordinates(x, y, r);
		for (Point point : pointCollection)
		{
			colorCollection.add(retrieveColor(point.x, point.y));
		}
		
		
		Color color = combineColors (colorCollection);
		
		circle.setFill(Color.TRANSPARENT);
		circle.setStroke(color);
        
		circle.setStrokeWidth(10);
		root.getChildren().add(circle);
	}
	
	private void createCropCircle(int x, int y, int r)
	{
		Circle circle = new Circle();
		circle.setCenterX(x);
		circle.setCenterY(y);
		circle.setRadius(r);
		
		List<Color> colorCollection = new ArrayList<Color>();
		List<Point> pointCollection = findCoordinates(x, y, r);
		for (Point point : pointCollection)
		{
			colorCollection.add(retrieveColor(point.x, point.y));
		}

		Color color = combineColors (colorCollection);
		
		circle.setFill(color);
		root.getChildren().add(circle);
	}

	private List<Point> findCoordinates(int x, int y, int r)
	{
		List<Point> pointCollection = new ArrayList<Point>();
		for(int i = x-(r); i <= x+r; i+=10)
		{
			for(int j = y-r; j <= y+r; j+=10)
			{
				if (j>0 && j < height && i > 0 && i < width)
				{
					pointCollection.add(new Point(i, j));
				}
			}
		}
		
		return pointCollection;
	}
	
	private Color retrieveColor(int x, int y)
	{
		PixelReader reader = cropsImage.getPixelReader();
		Color color = reader.getColor(x, y);
		return color;
	}
	
	private Color combineColors(List<Color> cc)
	{
		double r = 0;
		double g = 0;
		double b = 0;
		
		for (Color color : cc)
		{
			r+= color.getRed();
			g+= color.getGreen();
			b+= color.getBlue();
			
		}
		
		r/=cc.size();
		g/=cc.size();
		b/=cc.size();
		

		return Color.color(r+((1-r)/4),g+((1-g)/4),b+((1-b)/4),.6);

	}
	
	public void createFile()
	{
		File file = new File("CCField.png");
		WritableImage image = root.snapshot(null, null);
        try 
        {
            ImageIO.write(SwingFXUtils.fromFXImage(image, null), "png", file);
        } 
        catch (Exception s) 
        {
        	System.out.println(s);
        }
	}
	
	EventHandler<MouseEvent> mouseHandler = new EventHandler<MouseEvent>() 
			{	 
	        @Override
	        public void handle(MouseEvent mouseEvent) 
	        {

	        	Point2D coordinates = new Point2D(mouseEvent.getX(),mouseEvent.getY());        	
	        	createRandomCropCircle((int)coordinates.getX(), (int)coordinates.getY());
	        }
			};
	
	private void createRandomCropCircle(int x, int y)
	{
		Random rand = new Random();
		int num = rand.nextInt(5);
		switch (num){
		case 0:
			createCropCircle(x, y, 40);
			break;
		case 1:
			createCropCircle(x, y, 30);
			createRing(x, y, 80);
			break;
		case 2:
			createCropCircle(x, y, 40);
			createRing(x, y, 80);
			createRing(x, y, 120);
			break;
		case 3:
			createRing(x, y, 80);
			createRing(x, y, 120);
			break;
		case 4:
			createCropCircle(x, y, 30);
			createRing(x, y, 80);
			createRing(x, y, 120);
			createRing(x, y, 180);
			break;
		}
	}
	
	
	
	
	public static void main(String[] args) 
	{
		//filename = args[0];
		filename = "Field.jpg";
		launch(args);
	}

}

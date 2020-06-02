import java.applet.*;
import java.awt.*;

public class gui extends Applet{
	public void paint(Graphics g)
	{
		Font f=new Font("Sherif",Font.BOLD,500);
		setFont(f);
		g.setColor(Color.red);
		g.drawString("Rizwan", 20, 20);
	}
}

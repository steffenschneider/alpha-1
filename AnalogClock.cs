using System;
using System.Windows;
using System.Diagnostics;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;
using System.Drawing;

// XAML
// draw three lines in XAML and give them the appropriate name

namespace WpfApplication1
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            
            System.Windows.Threading.DispatcherTimer dispatcherTimer = new System.Windows.Threading.DispatcherTimer();
            dispatcherTimer.Tick += dispatcherTimer_Tick;
            dispatcherTimer.Interval = new TimeSpan(0, 0, 0, 0, 50);
            dispatcherTimer.Start();
        }

        private void dispatcherTimer_Tick(object sender, EventArgs e)
        {
            DateTime time = DateTime.Now;
            int xOrigin = 110;
            int yOrigin = 110;
            int milliSecond = time.Millisecond;
            int second = time.Second;
            int minute = time.Minute;
            int hour = time.Hour;

            double radSecond = (second + 1.0 * milliSecond / 1000.0) * 6.0 / 180.0 * Math.PI;
            LineSecond.X2 = Math.Sin(radSecond) * 80 + xOrigin;
            LineSecond.Y2 = -(Math.Cos(radSecond) * 80) + yOrigin;

            double radMinute = (minute + 1.0 * second / 60.0) * 6.0 / 180.0 * Math.PI;
            LineMinute.X2 = Math.Sin(radMinute) * 80 + xOrigin;
            LineMinute.Y2 = -(Math.Cos(radMinute) * 80) + yOrigin;

            // Because hour pointer is not only moving every hour
            double radHour = (hour + 1.0 * minute / 60.0) * 30.0 / 180.0 * Math.PI;
            LineHour.X2 = Math.Sin(radHour) * 55 + xOrigin;
            LineHour.Y2 = -(Math.Cos(radHour) * 55) + yOrigin;
        }
    }
}

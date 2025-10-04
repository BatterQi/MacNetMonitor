import rumps
import psutil
import time

class NetworkSpeedApp(rumps.App):
    def __init__(self):
        super(NetworkSpeedApp, self).__init__("🌐")
        self.last_bytes_sent = psutil.net_io_counters().bytes_sent
        self.last_bytes_recv = psutil.net_io_counters().bytes_recv
        self.last_time = time.time()
        self.timer = rumps.Timer(self.on_tick, 1)  # 每秒更新一次
        self.timer.start()

    def format_bytes(self, bytes_per_sec):
        """将字节/秒转换为合适的单位（B/s, KB/s, MB/s）"""
        if bytes_per_sec < 1024:
            return f"{bytes_per_sec:.0f} B/s"
        elif bytes_per_sec < 1024**2:
            return f"{bytes_per_sec / 1024:.1f} KB/s"
        else:
            return f"{bytes_per_sec / (1024**2):.1f} MB/s"

    def on_tick(self, _):
        # 获取当前网络数据
        net = psutil.net_io_counters()
        current_bytes_sent = net.bytes_sent
        current_bytes_recv = net.bytes_recv
        current_time = time.time()

        # 计算时间差
        time_diff = current_time - self.last_time
        if time_diff <= 0:
            return

        # 计算每秒字节数
        sent_speed = (current_bytes_sent - self.last_bytes_sent) / time_diff
        recv_speed = (current_bytes_recv - self.last_bytes_recv) / time_diff

        # 更新标题（菜单栏显示）
        title = f"↓{self.format_bytes(recv_speed)} ↑{self.format_bytes(sent_speed)}"
        self.title = title

        # 更新历史值
        self.last_bytes_sent = current_bytes_sent
        self.last_bytes_recv = current_bytes_recv
        self.last_time = current_time

if __name__ == "__main__":
    NetworkSpeedApp().run()

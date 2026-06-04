class DycLogger:
    def get_logger(self):
        import sys
        from loguru import logger
        import inspect

        frame_info = inspect.stack()[1]
        calling_module = inspect.getmodule(frame_info[0]).__file__.split("\\")[-1]
        calling_line = frame_info.lineno

        logger.configure(handlers=[
            {
                "sink": sys.stdout,
                "format": "<level>{time:YYYY-MM-DD HH:mm:ss.SSS}</level> | " + calling_module + " (line " + str(
                    calling_line) + ") | <level>{level} | {message}</level>",
                "colorize": True
            }, {
                "sink": "logs/{time:YYYY-MM-DD}.log",  # 指定日志文件路径，使用日期作为文件名的一部分
                "format": "<level>{time:YYYY-MM-DD HH:mm:ss.SSS}</level> | " + calling_module + " (line " + str(
                    calling_line) + ") | <level>{level} | {message}</level>",
                "level": "DEBUG",
                "rotation": "1 day"  # 每天创建一个新的日志文件
            }
        ])

        return logger

# lg=DycLogger()
# lg.get_logger().info("hello world")
# lg.get_logger().debug("hello world")
# lg.get_logger().warning("hello world")
# lg.get_logger().error("hello world")
# lg.get_logger().critical("hello world")

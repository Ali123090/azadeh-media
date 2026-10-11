# صف انتشار بله

هر فایل JSON در این پوشه یک پست است. اسکریپت bale_publisher.py روی کامپیوتر داخل ایران هر ۱۵ دقیقه این پوشه را می‌خواند و پست‌هایی که زمانشان رسیده را منتشر می‌کند.

نمونه:

```json
{
  "publish_at": "2026-10-12T21:00:00+03:30",
  "type": "photo",
  "media": "stories/2026-10-11/story4-cold-antibiotic.png",
  "caption": "متن پست"
}
```

type: text | photo | video | document
برای غیرفعال کردن یک پست: "enabled": false

"""Populate CareerBridge with a varied, presentation-ready opportunity catalog."""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "careerbridge.settings")
django.setup()

from opportunities.models import Opportunity


# Arabic title, English title, company, category, Arabic location, English location,
# Arabic description, English description, remote-friendly
items = [
    ("مساعد مطوّر Django", "Junior Django Developer", "Nexa Studio", "development", "عن بُعد", "Remote", "ساهم في بناء واجهات ولوحة إدارة لمنصة تعليمية.", "Help build interfaces and an admin workspace for an education platform.", True),
    ("متدرب تصميم واجهات", "UI Design Intern", "Nova Labs", "design", "دمشق", "Damascus", "حوّل الأفكار إلى شاشات واضحة ومتجاوبة مع فريق منتج متعاون.", "Turn product ideas into clear responsive screens with a collaborative product team.", False),
    ("مساعد تسويق رقمي", "Digital Marketing Assistant", "Orbit", "marketing", "عن بُعد", "Remote", "شارك في حملات نموّ حقيقية وتعلّم من فريق متخصص.", "Support real growth campaigns and learn with a specialist team.", True),
    ("مطوّر Frontend مبتدئ", "Junior Frontend Developer", "PixelCraft", "development", "حلب", "Aleppo", "ابنِ مكونات واجهات حديثة باستخدام React وواجهات API.", "Build modern interface components with React and API integrations.", False),
    ("محلل بيانات متدرب", "Data Analyst Intern", "Insight Labs", "data", "عن بُعد", "Remote", "حلّل بيانات المبيعات وأنشئ لوحات متابعة مفهومة.", "Analyze sales data and create clear reporting dashboards.", True),
    ("كاتب محتوى تقني", "Technical Content Writer", "CodeSphere", "content", "عن بُعد", "Remote", "اكتب أدلة مبسطة ومحتوى مفيد للمطورين الجدد.", "Write approachable guides and useful content for new developers.", True),
    ("مصمم هوية بصرية", "Brand Identity Designer", "Mosaic Agency", "design", "دمشق", "Damascus", "طوّر أنظمة هوية بصرية وحملات رقمية لعلامات ناشئة.", "Develop visual identity systems and digital campaigns for emerging brands.", False),
    ("منسق نجاح العملاء", "Customer Success Coordinator", "CloudNine", "business", "عن بُعد", "Remote", "ساعد العملاء على الاستفادة من منتجات SaaS وتحسين تجربتهم.", "Help clients get value from SaaS products and improve their experience.", True),
    ("متدرب أمن سيبراني", "Cybersecurity Intern", "ShieldWorks", "security", "دمشق", "Damascus", "تعلّم أساسيات اختبار الحماية ومتابعة التنبيهات الأمنية.", "Learn security testing fundamentals and help monitor security alerts.", False),
    ("مساعد مدير مشروع", "Project Management Assistant", "BridgePoint", "business", "عن بُعد", "Remote", "نظّم المهام واجتماعات الفريق وساهم في تسليم المشاريع.", "Coordinate tasks and team meetings to help deliver projects smoothly.", True),
    ("متدرب موارد بشرية", "HR Operations Intern", "PeopleFirst", "human resources", "حمص", "Homs", "ادعم عمليات التوظيف والتواصل مع المرشحين وتنظيم الملفات.", "Support recruiting operations, candidate communication, and document organization.", False),
    ("مطور تطبيقات Flutter", "Flutter Developer Intern", "MobileMint", "development", "عن بُعد", "Remote", "ساهم في تطوير تطبيقات موبايل سريعة وسهلة الاستخدام.", "Contribute to fast, user-friendly mobile application development.", True),
    ("أخصائي تحسين محركات البحث", "SEO Specialist", "SearchSpring", "marketing", "عن بُعد", "Remote", "حسّن محتوى المواقع وراقب أداء الكلمات المفتاحية.", "Optimize website content and track keyword performance.", True),
    ("باحث تجربة المستخدم", "UX Research Assistant", "Humanly", "design", "دمشق", "Damascus", "نفّذ مقابلات مستخدمين وحوّل الملاحظات إلى فرص تحسين.", "Run user interviews and turn insights into improvement opportunities.", False),
    ("متدرب ذكاء اصطناعي", "AI Research Intern", "Neuron Hub", "data", "عن بُعد", "Remote", "جرّب نماذج تعلم آلي وساعد في تقييم جودة النتائج.", "Experiment with machine-learning models and help evaluate their outputs.", True),
    ("محرر فيديو قصير", "Short-form Video Editor", "FrameLab", "content", "اللاذقية", "Latakia", "حرّر فيديوهات قصيرة لحملات اجتماعية ومنصات المحتوى.", "Edit short videos for social campaigns and content platforms.", False),
    ("مسؤول مبيعات داخلية", "Inside Sales Representative", "LaunchPad", "sales", "عن بُعد", "Remote", "تواصل مع العملاء المحتملين وساعد في بناء فرص البيع.", "Connect with prospective clients and help build sales opportunities.", True),
    ("مساعد محاسب", "Junior Accounting Assistant", "LedgerLine", "finance", "دمشق", "Damascus", "نظّم الفواتير وساعد في إعداد التقارير المالية الأساسية.", "Organize invoices and help prepare foundational financial reports.", False),
    ("اختبار جودة برمجيات", "QA Tester", "BrightStack", "development", "عن بُعد", "Remote", "اختبر ميزات المنتج وسجّل الحالات لضمان تجربة مستقرة.", "Test product features and document cases to ensure a reliable experience.", True),
    ("مدير مجتمع", "Community Manager", "Gatherly", "marketing", "عن بُعد", "Remote", "ابنِ تفاعلًا مفيدًا مع مجتمع المنتج عبر المنصات الرقمية.", "Build meaningful engagement with the product community across digital channels.", True),
    ("متدرب لوجستيات", "Logistics Intern", "RouteX", "operations", "حماة", "Hama", "تابع الشحنات ونظّم البيانات التشغيلية مع فريق اللوجستيات.", "Track shipments and organize operational data with the logistics team.", False),
    ("مساعد قانوني", "Legal Assistant", "LexPoint", "legal", "دمشق", "Damascus", "ادعم مراجعة العقود وتنظيم الملفات القانونية الداخلية.", "Support contract review and internal legal document organization.", False),
    ("مطوّر WordPress", "WordPress Developer", "SiteForge", "development", "عن بُعد", "Remote", "أنشئ مواقع أعمال سريعة ومرنة لعملاء متنوعين.", "Build fast, flexible business websites for a range of clients.", True),
    ("منسق فعاليات", "Events Coordinator", "Spark Events", "operations", "دمشق", "Damascus", "خطّط للفعاليات وساعد في إدارة التجربة من البداية إلى النهاية.", "Plan events and help manage the experience end to end.", False),
    ("مصمم موشن غرافيك", "Motion Graphics Designer", "MotionMint", "design", "عن بُعد", "Remote", "أنشئ رسومًا متحركة خفيفة للمحتوى التسويقي والمنتج.", "Create lightweight animations for product and marketing content.", True),
    ("مساعد بحث سوق", "Market Research Assistant", "MarketMap", "business", "عن بُعد", "Remote", "اجمع رؤى عن المنافسين والعملاء لدعم قرارات المنتج.", "Gather competitor and customer insights to support product decisions.", True),
    ("متدرب دعم تقني", "Technical Support Intern", "HelpDesk Pro", "support", "حلب", "Aleppo", "ساعد المستخدمين في حل المشكلات التقنية وتوثيق الحلول.", "Help users resolve technical issues and document helpful solutions.", False),
    ("مترجم عربي إنجليزي", "Arabic-English Translator", "LinguaWorks", "content", "عن بُعد", "Remote", "ترجم محتوى رقميًا مع الحفاظ على وضوح النبرة والسياق.", "Translate digital content while preserving tone, clarity, and context.", True),
    ("محلل عمليات", "Operations Analyst", "Flowline", "operations", "عن بُعد", "Remote", "راقب العمليات وحدد فرصًا عملية لتحسين الكفاءة.", "Monitor operations and identify practical opportunities to improve efficiency.", True),
    ("متدرب تصميم منتجات", "Product Design Intern", "Venture Studio", "design", "دمشق", "Damascus", "تعاون مع فريق المنتج لتحويل مشاكل المستخدمين إلى حلول واضحة.", "Collaborate with the product team to turn user problems into clear solutions.", False),
]

created = 0
for title_ar, title_en, company, category, location_ar, location_en, description_ar, description_en, is_remote in items:
    _, was_created = Opportunity.objects.get_or_create(
        title_en=title_en,
        company=company,
        defaults={
            "title_ar": title_ar,
            "category": category,
            "location_ar": location_ar,
            "location_en": location_en,
            "description_ar": description_ar,
            "description_en": description_en,
            "is_remote": is_remote,
        },
    )
    created += was_created

print(f"CareerBridge catalog is ready: {Opportunity.objects.count()} opportunities ({created} added).")

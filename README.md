# linearizedPDF

```bash
# linearize PDF 변환
$ qpdf --linearize us-public-health-and-welfare-code.pdf us-public-health-and-welfare-code.linearized.pdf

$ qpdf --linearize "all-products_esuprt_printers_main_esuprt_printers_mono_laser_dell-b5465dnf_user's_guide_ko-kr.pdf" "all-products_esuprt_printers_main_esuprt_printers_mono_laser_dell-b5465dnf_user's_guide_ko-kr.linearized.pdf"

$ qpdf --linearize compressed.tracemonkey-pldi-09.pdf compressed.tracemonkey-pldi-09.linearized.pdf
# linearize PDF 확인
$ sed '4q;d' us-public-health-and-welfare-code.linearized.pdf
$ qpdf --check-linearization us-public-health-and-welfare-code.linearized.pdf
$ qpdf --show-linearization us-public-health-and-welfare-code.linearized.pdf

$ sed '4q;d' "all-products_esuprt_printers_main_esuprt_printers_mono_laser_dell-b5465dnf_user's_guide_ko-kr.linearized.pdf"
$ qpdf --check-linearization "all-products_esuprt_printers_main_esuprt_printers_mono_laser_dell-b5465dnf_user's_guide_ko-kr.linearized.pdf"
$ qpdf --show-linearization "all-products_esuprt_printers_main_esuprt_printers_mono_laser_dell-b5465dnf_user's_guide_ko-kr.linearized.pdf"
```

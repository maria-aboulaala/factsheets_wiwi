document.addEventListener('DOMContentLoaded', function() {
    var button = document.getElementById('download-pdf-button');
    button.onclick = function() {
        html2canvas(document.querySelector("#content-to-capture")).then(canvas => {
            const imgData = canvas.toDataURL('image/png');
            const pdf = new jsPDF({
                orientation: 'landscape',
            });
            const imgProps= pdf.getImageProperties(imgData);
            const pdfWidth = pdf.internal.pageSize.getWidth();
            const pdfHeight = (imgProps.height * pdfWidth) / imgProps.width;
            pdf.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight);
            pdf.save("download.pdf");
        });
    };
});

document.addEventListener("DOMContentLoaded", function () {
    var script = document.createElement("script");
    script.id = "kapa-widget-script"
  
    script.src = "https://widget.kapa.ai/kapa-widget.bundle.js";
  
    script.setAttribute(data-website-id="88ce68c1-ce0d-452a-bb55-e05e3beaa240");
    script.setAttribute(data-project-name="UPPMAX");
    script.setAttribute(data-project-color="#D22B2B);
    script.setAttribute(data-project-logo="./assets/UU_logo_vit.svg");
    script.setAttribute(data-modal-image="./assets/UU_logo_color.svg");
    script.setAttribute(data-button-image="./assets/UU_logo_vit.svg");
    script.setAttribute(data-modal-disclaimer="This AI assistant is in development and may not always provide accurate information. Please submit your queries to the support team at https://supr.naiss.se/support");
 
    script.async = true;
    document.head.appendChild(script);
  });

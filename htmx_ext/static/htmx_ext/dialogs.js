;(function () {
  function getCurrentModalInstance(){
    const el = document.getElementById('modal')

    if (el) {
      return bootstrap.Modal.getInstance(el) // Returns a Bootstrap modal instance
    }

    return null
  }


  htmx.on("htmx:afterSwap", (e) => {
    if (e.detail.target.id === "dialog") {
      console.log('htmx:afterSwap')
    }
  })

  htmx.on("htmx:beforeSwap", (e) => {
    /*
      Intercept the HTMx swap event and according to custom http status codes close or
      not open modal windows.

      HX_STATUS_UPDATE = 280
      HX_STATUS_CREATE = 281
      HX_STATUS_DELETE = 282
    */
    if (e.detail.xhr.status===280 || e.detail.xhr.status===281 || e.detail.xhr.status===282) {
      modal = getCurrentModalInstance()

      if (modal)
        modal.hide()
    }
  })

  htmx.on("hidden.bs.modal", () => {
    document.getElementById("dialog").innerHTML = ""
  })

  document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('modal').addEventListener('show.bs.modal', function(event) {
        const trigger = event.relatedTarget;
        if (trigger) {
            const modalSize = trigger.getAttribute('data-modal-size') || 'modal-lg';
            const modalDialog = this.querySelector('.modal-dialog');

            modalDialog.classList.remove('modal-sm', 'modal-lg', 'modal-xl', 'modal-fullscreen');

            if (modalSize) {
                modalDialog.classList.add(modalSize);
            }
        }
    });

    document.getElementById('modal').addEventListener('hidden.bs.modal', function() {
        const modalDialog = this.querySelector('.modal-dialog');
        modalDialog.classList.remove('modal-sm', 'modal-lg', 'modal-xl', 'modal-fullscreen');
        modalDialog.classList.add('modal-lg');
    });
  });
})()

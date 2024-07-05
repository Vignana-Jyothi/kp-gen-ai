$(document).ready(function () {
    let currentPost = 1;
    const totalPosts = $(".post-item").length;
    $("#post-" + currentPost).show();

    $("#next-btn").click(function () {
        if (currentPost < totalPosts) {
            $("#post-" + currentPost).hide();
            currentPost++;
            $("#post-" + currentPost).show();
        }
        updateNavButtons();
    });

    $("#prev-btn").click(function () {
        if (currentPost > 1) {
            $("#post-" + currentPost).hide();
            currentPost--;
            $("#post-" + currentPost).show();
        }
        updateNavButtons();
    });

    function updateNavButtons() {
        if (currentPost === 1) {
            $("#prev-btn").prop("disabled", true);
        } else {
            $("#prev-btn").prop("disabled", false);
        }

        if (currentPost === totalPosts) {
            $("#next-btn").prop("disabled", true);
        } else {
            $("#next-btn").prop("disabled", false);
        }
    }

    $(".feedback-form").submit(function (e) {
        e.preventDefault();
        const form = $(this);
        const action = form.find("button[type=submit]:focus").val();
        const loader = form.siblings(".loader");
        const postContentDiv = form.find(".post-content");

        // Only require fields for "Improve" action
        if (action === "improve") {
            form.find("[name=content_rating], [name=content_comment], [name=structure_rating], [name=structure_comment]").prop("required", true);
        } else {
            form.find("[name=content_rating], [name=content_comment], [name=structure_rating], [name=structure_comment]").prop("required", false);
        }

        loader.show();
        form.hide();

        $.ajax({
            type: "POST",
            url: "/submit_feedback",
            data: form.serialize() + "&action=" + action,
            success: function (response) {
                loader.hide();
                form.show();
                if (action === "improve") {
                    postContentDiv.html(response.improved_content);
                } else {
                    triggerConfetti();
                }
            },
            error: function () {
                loader.hide();
                form.show();
                alert("Error submitting feedback.");
            }
        });
    });

    function triggerConfetti() {
        const duration = 2 * 1000;
        const animationEnd = Date.now() + duration;
        const defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 0 };

        function randomInRange(min, max) {
            return Math.random() * (max - min) + min;
        }

        const interval = setInterval(function() {
            const timeLeft = animationEnd - Date.now();

            if (timeLeft <= 0) {
                return clearInterval(interval);
            }

            const particleCount = 50 * (timeLeft / duration);
            // since particles fall down, start a bit higher than random
            confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 } }));
            confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 } }));
        }, 250);
    }
});

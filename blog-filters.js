(function () {
  const filters = document.querySelectorAll(".blog-filter-pill");
  const cards = document.querySelectorAll(".blog-list .blog-card");
  const emptyState = document.querySelector(".blog-empty-state");
  if (!filters.length || !cards.length) return;

  filters.forEach((pill) => {
    pill.addEventListener("click", () => {
      const filter = pill.dataset.filter;
      filters.forEach((p) => p.classList.toggle("is-active", p === pill));

      let visibleCount = 0;
      cards.forEach((card) => {
        const match = filter === "all" || card.dataset.category === filter;
        card.hidden = !match;
        if (match) visibleCount++;
      });

      if (emptyState) emptyState.hidden = visibleCount !== 0;
    });
  });
})();

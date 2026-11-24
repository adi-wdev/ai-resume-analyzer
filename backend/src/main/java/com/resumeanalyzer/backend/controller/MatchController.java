package com.resumeanalyzer.backend.controller;

import com.resumeanalyzer.backend.dto.MatchResult;
import com.resumeanalyzer.backend.service.MatchService;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/matches")
public class MatchController {

    private final MatchService matchService;

    public MatchController(MatchService matchService) {
        this.matchService = matchService;
    }

    @GetMapping("/candidate/{candidateId}/job/{jobId}")
    public ResponseEntity<MatchResult> calculateMatch(
            @PathVariable Long candidateId,
            @PathVariable Long jobId
    ) {

        MatchResult result = matchService.calculateMatch(
                candidateId,
                jobId
        );

        return ResponseEntity.ok(result);
    }
}